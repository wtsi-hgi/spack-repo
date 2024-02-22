# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDevrate(RPackage):
	"""Quantify the Relationship Between Development Rate and
Temperature in Ectotherms

	A set of functions to quantify the relationship between development
    rate and temperature and to build phenological models. The package comprises 
    a set of models and estimated parameters borrowed from a literature review 
    in ectotherms. The methods and literature review are described in Rebaudo 
    et al. (2018) <doi:10.1111/2041-210X.12935>, Rebaudo and Rabhi (2018) 
    <doi:10.1111/eea.12693>, and Regnier et al. (2021) <doi:10.1093/ee/nvab115>. 
    An example can be found in Rebaudo et al. (2017) 
    <doi:10.1007/s13355-017-0480-5>. 
	"""
	
	homepage = "https://github.com/frareb/devRate/"
	cran = "devRate" 

	version("0.2.4", md5="f761053700035e12ba352f533ded09cb")

	depends_on("r@3.5:", type=("build", "run"))
