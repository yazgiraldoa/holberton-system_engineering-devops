#!/usr/bin/env ruby
# Regular expression only matching: capital letters
puts ARGV[0].scan(/[A-Z]/).join
