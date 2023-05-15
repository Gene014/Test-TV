# Import program from another program
from TV import TV

# Create 2 instances for Television
tv1=TV()
tv2=TV()

# Settings for TV1
tv1.setChannel(30)
tv1.setVolume(3)

# Settings for TV2
tv2.setChannel(3)
tv2.setVolume(2)

# Print the desired settings for both TV
print("\n\33[96m\33[1mtv1's channel is\33[32m",tv1.getChannel(),
      "\33[96m\33[1mand volume level is\33[32m",tv1.getVolume())

print("\n\33[96m\33[1mtv2's channel is\33[32m",tv2.getChannel(),
      "\33[96m\33[1mand volume level is\33[32m",tv2.getVolume())