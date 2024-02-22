# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProffer(RPackage):
	"""Profile R Code and Visualize with 'Pprof'

	Like similar profiling tools,
  the 'proffer' package automatically detects
  sources of slowness in R code.
  The distinguishing feature of 'proffer' is its utilization of
  'pprof', which supplies interactive visualizations
  that are efficient and easy to interpret.
  Behind the scenes, the 'profile' package converts
  native Rprof() data to a protocol buffer
  that 'pprof' understands.
  For the documentation of 'proffer',
  visit <https://r-prof.github.io/proffer/>.
  To learn about the implementations and methodologies of
  'pprof', 'profile', and protocol buffers,
  visit <https://github.com/google/pprof>.
  <https://developers.google.com/protocol-buffers>,
  and <https://github.com/r-prof/profile>, respectively.
	"""
	
	homepage = "https://github.com/r-prof/proffer"
	cran = "proffer" 

	version("0.1.6", md5="0379a3e55a9a91bd69303453e27b715d")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-cli@2:", type=("build", "run"))
	depends_on("r-parallelly@1.26:", type=("build", "run"))
	depends_on("r-pingr@2.0.1:", type=("build", "run"))
	depends_on("r-processx@3.4:", type=("build", "run"))
	depends_on("r-profile@1:", type=("build", "run"))
	depends_on("r-rprotobuf@0.4.14:", type=("build", "run"))
	depends_on("r-withr@2.1.2:", type=("build", "run"))
	depends_on("graphviz", type=("build", "link", "run"))
