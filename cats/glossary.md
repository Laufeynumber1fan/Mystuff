Wire size         size of the frame on the actual wire / air
Capture size      amount of bytes kept of the frame in the capture file. Cannot exceed wire size, but can be less.
Slicing           cutting away bytes from a frame (meaning, "capture size" < "wire size")
Hard Slicing      cutting bytes and setting capture and wire size to the new (short) length
Soft Slicing      cutting bytes and adjusting only capture size to the new (short) length while keeping wire size intact
Adaptive Slicing  cutting on offsets depending on header sizes, e.g "after the TCP header" or "after the IPv6 header"
Static Slicing    cutting at a specific offset, regardless of frame headers
External Slicing  cutting is performed on a device not doing the capture. This often results in hard sliced captures.
z