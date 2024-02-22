# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMdftracks(RPackage):
	"""Read and Write 'MTrackJ Data Files'

	'MTrackJ' is an 'ImageJ' plugin for motion tracking and analysis (see 
    <https://imagescience.org/meijering/software/mtrackj/>). This package reads 
    and writes 'MTrackJ Data Files' ('.mdf', see 
    <https://imagescience.org/meijering/software/mtrackj/format/>). It supports
    2D data and read/writes cluster, point, and channel information. If desired, 
    generates track identifiers that are unique over the clusters.
    See the project page for more information and examples.
	"""
	
	homepage = "https://github.com/burgerga/mdftracks"
	cran = "mdftracks" 

	version("0.2.2", md5="71eeb96f45287832c3c9b55adcd4d8aa")

	depends_on("r@2.10:", type=("build", "run"))
