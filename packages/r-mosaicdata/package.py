# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMosaicdata(RPackage):
	"""Project MOSAIC Data Sets

	Data sets from Project MOSAIC (<http://www.mosaic-web.org>) used
    to teach mathematics, statistics, computation and modeling.  Funded by the
    NSF, Project MOSAIC is a community of educators working to tie together
    aspects of quantitative work that students in science, technology,
    engineering and mathematics will need in their professional lives, but
    which are usually taught in isolation, if at all.
	"""
	
	homepage = "https://github.com/ProjectMOSAIC/mosaicData"
	cran = "mosaicData" 

	version("0.20.4", md5="4fdb8a2fa2f0b35327ec2f6c6da5b5ce")

	depends_on("r@4.1:", type=("build", "run"))
