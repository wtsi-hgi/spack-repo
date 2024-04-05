# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRveg(RPackage):
	"""Digitization of Phytosociological Relevés

	Simple and fast tool for transforming phytosociological 
    vegetation data into digital form for the following analysis.
    Danihelka, Chrtek, and Kaplan (2012, ISSN:00327786).
    Hennekens, and Schaminée (2001) <doi:10.2307/3237010>.
    Tichý (2002) <doi:10.1111/j.1654-1103.2002.tb02069.x>.
    Wickham, François, Henry, Müller (2022) <https://CRAN.R-project.org/package=dplyr>.
	"""
	
	homepage = "https://plant-ecology-lab-czu.com/rveg/"
	cran = "Rveg" 

	version("0.1.4", md5="3e8ffface8f07eedf84abf535a882c7f")
	version("0.1.3", md5="2641602847448e83ac49bc069d9be728")

	depends_on("r-dplyr", type=("build", "run"))
