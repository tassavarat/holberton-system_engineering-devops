#!/usr/bin/env ruby
# Regular expression to match repetitions

puts ARGV[0].scan(/hb{0,1}tn/).join
