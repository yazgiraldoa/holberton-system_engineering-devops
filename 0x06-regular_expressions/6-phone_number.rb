#!/usr/bin/env ruby
# Regular expression only matching: a 10 digit phone number
puts ARGV[0].scan(/^\d{10}$/).join
