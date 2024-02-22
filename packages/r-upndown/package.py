# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUpndown(RPackage):
	"""Utilities and Design Aids for Up-and-Down Dose-Finding Studies

	Up-and-Down is the most popular design approach for dose-finding, but has been severely under-served by the statistical computing community. This is the first package to address Up-and-Down's needs. For a recent methodological tutorial on Up-and-Down, see Oron et al. (2022) <doi:10.1097/ALN.0000000000004282>.
	"""
	
	cran = "upndown" 

	version("0.1.0", md5="5622f4ce0deb346c83852ff63787f021")

	depends_on("r-cir", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-numbers", type=("build", "run"))
