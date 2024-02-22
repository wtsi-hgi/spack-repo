# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElisr(RPackage):
	"""Exploratory Likert Scaling

	An alternative to Exploratory Factor Analysis (EFA) for
    metrical data in R. Drawing on characteristics of classical test
    theory, Exploratory Likert Scaling (ELiS) supports the user exploring
    multiple one-dimensional data structures. In common research practice,
    however, EFA remains the go-to method to uncover the (underlying)
    structure of a data set. Orthogonal dimensions and the potential of
    overextraction are often accepted as side effects. As described in
    Müller-Schneider (2001) <doi:10.1515/zfsoz-2001-0404>), ELiS confronts
    these problems. As a result, 'elisr' provides the platform to fully
    exploit the exploratory potential of the multiple scaling approach
    itself.
	"""
	
	homepage = "https://github.com/sbissantz/elisr"
	cran = "elisr" 

	version("0.1.1", md5="4c111459c9db878a5701be44c4e40ae9")

	depends_on("r@4:", type=("build", "run"))
