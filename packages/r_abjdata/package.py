# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbjdata(RPackage):
	"""Databases Used Routinely by the Brazilian Jurimetrics
Association

	The Brazilian Jurimetrics Association (ABJ in
    Portuguese, see <https://abj.org.br/> for more information) is
    a non-profit organization which aims to investigate and promote the
    use of statistics and probability in the study of Law and its
    institutions. This package has a set of datasets commonly used in
    our book.
	"""
	
	homepage = "https://abjur.github.io/abjData/"
	cran = "abjData" 

	version("1.1.2", md5="ce34560a5a10c39d49192ffc2ad5cd9b")

	depends_on("r@3.3.1:", type=("build", "run"))
