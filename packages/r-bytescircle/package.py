# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBytescircle(RPackage):
	"""Statistics About Bytes Contained in a File as a Circle Plot

	Shows statistics about bytes contained in a file 
  as a circle graph of deviations from mean in sigma increments. 
  The function can be useful for statistically analyze the content of files 
  in a glimpse: text files are shown as a green centered crown, compressed 
  and encrypted files should be shown as equally distributed variations with 
  a very low CV (sigma/mean), and other types of files can be classified between 
  these two categories depending on their text vs binary content, which can be 
  useful to quickly determine how information is stored inside them (databases, 
  multimedia files, etc). 
	"""
	
	cran = "bytescircle" 

	version("1.1.2", md5="5db78abee20febea4d365be0b378093f")

	depends_on("r@3.3.1:", type=("build", "run"))
