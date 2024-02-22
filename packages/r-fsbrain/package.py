# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFsbrain(RPackage):
	"""Managing and Visualizing Brain Surface Data

	Provides high-level access to neuroimaging data from standard software packages like 'FreeSurfer' <http://freesurfer.net/> on the level of subjects and groups. Load morphometry data, surfaces and brain parcellations based on atlases. Mask data using labels, load data for specific atlas regions only, and visualize data and statistical results directly in 'R'.
	"""
	
	homepage = "https://github.com/dfsp-spirit/fsbrain"
	cran = "fsbrain" 

	version("0.5.5", md5="08204b85bcd9d2687413e20b698fe89a")

	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-freesurferformats@0.1.17:", type=("build", "run"))
	depends_on("r-pkgfilecache@0.1.1:", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-squash", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
