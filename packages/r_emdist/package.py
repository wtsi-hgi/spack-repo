# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmdist(RPackage):
	"""Earth Mover's Distance

	Package providing calculation of Earth Mover's Distance (EMD).
	"""
	
	homepage = "http://www.rforge.net/emd"
	cran = "emdist" 

	version("0.3-3", md5="184e126bb29ed5a079b1c8ea11402770")

	depends_on("r@2.3:", type=("build", "run"))
