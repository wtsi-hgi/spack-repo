# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDevemf(RPackage):
	"""EMF Graphics Output Device

	Output graphics to EMF+/EMF.
	"""
	
	homepage = "https://github.com/plfjohnson/devEMF"
	cran = "devEMF" 

	version("4.4-2", md5="1da629a258772141fa10a1b82505369c")

	depends_on("r@2.10.1:", type=("build", "run"))
	depends_on("fontconfig", type=("build", "link", "run"))
	depends_on("zlib", type=("build", "link", "run"))
