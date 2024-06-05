#!/usr/bin/env ruby
# read output of
# ```
# curl -s -g 
# "https://www.math.bgu.ac.il/api/v1/courses?filter[lecturer_id]=37&include=generic_course,term"
# ```
#
require 'optparse'
require 'date'
require 'yaml'
require 'json'
require 'fileutils'

@script = File.basename($0)
@rcfile = ".#{@script}"

begin
  binding.eval(File.read(@rcfile), @rcfile)
rescue Errno::ENOENT => e
end

OptParse.new do |opts|
  opts.banner = <<EOF
Usage: #{@script} [options]

List issues on gitlab.

EOF

  opts.on('-h', '--help', 'Prints this help') do
    puts opts
    exit
  end
end.parse!

def presence(thing)
  (thing.nil? || thing.empty?) ? nil : thing
end

jsn = ARGF.read
cc=JSON.parse(jsn)
exit(1) unless cc['included'] && cc['data']
inc = {}
cc['included'].each do |ob|
  inc[ob['type']] ||= {}
  inc[ob['type']][ob['id']] = ob['attributes']
end
cc['data'].each do |it|
  course = it['attributes']
  rel = it['relationships']
  gen = inc['generic_courses'][rel['generic_course']['data']['id']]
  term = inc['terms'][rel['term']['data']['id']]
  if (term['title_i18n']['en'] =~ /^(\d\d\d\d)\-\-(\d\d)\-\-(.)$/)
    trm = $3.tr('AB', 'fs')
    year = trm == 'f' ? $1 : "20#{$2}"
    ts = "20#{$2}#{trm}"
  end
  date = Date.parse(term['starts'])
  title = {}
  %w[en he].each do |loc|
    title[loc] = presence(course['title_i18n'][loc]) || gen['name_i18n'][loc]
  end
  lang = presence(title['he']).nil? ? 'en' : 'he'
  pre = {
    last_modified_at: Time.now.to_date.httpdate,
    date: date.httpdate,
    title: title,
    type: gen['graduate'] ? 'graduate' : 'undergrad',
    catalog: gen['shid'],
    year: year,
    term: trm == 'f' ? 'fall' : 'spring',
    lang:  lang,
    notes: { lang => 'notes.pdf' },
    venue: 'bgu',
  }
  content = presence(course['abstract_i18n'][lang]) ||
    gen['description_i18n'][lang]
  dname = "/tmp/_teaching/#{ts}"
  FileUtils.mkdir_p dname, verbose: true
  File.write("#{dname}/#{gen['slug']}.md",
             pre.transform_keys(&:to_s).to_yaml +
             "---\n\n" + "## תקציר\n#{content}\n")
end


