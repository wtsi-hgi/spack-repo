# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLabourr(RPackage):
	"""Classify Multilingual Labour Market Free-Text to Standardized
Hierarchical Occupations

	Allows the user to map multilingual free-text of occupations to a broad range
    of standardized classifications. The package facilitates automatic occupation coding
    (see, e.g., Gweon et al. (2017) <doi:10.1515/jos-2017-0006> and Turrell et al. (2019)
    <doi:10.3386/w25837>), where the ISCO to ESCO mapping is exploited to extend the
    occupations hierarchy, Le Vrang et al. (2014) <doi:10.1109/mc.2014.283>. Document
    vectorization is performed using the multilingual ESCO corpus. A method based on the 
    nearest neighbor search is used to suggest the closest ISCO occupation.
	"""
	
	homepage = "https://github.com/AleKoure/labourR"
	cran = "labourR" 

	version("1.0.0", md5="c31f57ac77bea1a8eca7881e27736559")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-cld2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stopwords", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
