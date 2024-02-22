# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrunnermunzel(RPackage):
	"""(Permuted) Brunner-Munzel Test

	Provides the functions for Brunner-Munzel test and
    permuted Brunner-Munzel test,
    which enable to use formula, matrix, and table as argument.
    These functions are based on Brunner and Munzel (2000)
     <doi:10.1002/(SICI)1521-4036(200001)42:1%3C17::AID-BIMJ17%3E3.0.CO;2-U>
    and Neubert and Brunner (2007) <doi:10.1016/j.csda.2006.05.024>,
    and are written with FORTRAN.
	"""
	
	homepage = "https://github.com/toshi-ara/brunnermunzel"
	cran = "brunnermunzel" 

	version("2.0", md5="519ce1a742391d9031c4ed61ff1c7737")

