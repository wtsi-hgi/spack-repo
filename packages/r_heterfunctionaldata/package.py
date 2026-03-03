# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHeterfunctionaldata(RPackage):
	"""Test of No Main and/or Interaction Effects in Functional Data

	Distribution free heteroscedastic tests for functional data. 
    The following tests are included in this package: test of no main treatment or contrast
    effect and no simple treatment effect given in 
    Wang, Higgins, and Blasi (2010) <doi:10.1016/j.spl.2009.11.016>,
    no main time effect, and no interaction effect based on 
    original observations given in Wang and Akritas (2010a) 
    <doi:10.1080/10485250903171621>
    and tests based on ranks given in Wang and Akritas (2010b)
    <doi:10.1016/j.jmva.2010.03.012>.
	"""
	
	cran = "HeterFunctionalData" 

	version("0.1.0", md5="0751bc4d86e6e673bbd6e14ac402016e")

	depends_on("r@3.1:", type=("build", "run"))
