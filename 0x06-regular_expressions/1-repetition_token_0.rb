#!/usr/bin/env ruby
# Regular expression only matching: two to five ocurrences of a letter
puts ARGV[0].scan(/hbt{2,5}n/).join
