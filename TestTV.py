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


print("tv1's channel is",tv1.getChannel(),
      "and volume level is",tv1.getVolume())
print("tv2's channel is",tv2.getChannel(),
      "and volume level is",tv2.getVolume())