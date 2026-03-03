# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsymmetricsords(RPackage):
	"""Asymmetric Second Order Rotatable Designs (AsymmetricSORDs)

	Response surface designs (RSDs) are widely used for Response Surface Methodology (RSM) based optimization studies, which aid in exploring the relationship between a group of explanatory variables and one or more response variable(s) (G.E.P. Box and K.B. Wilson (1951), "On the experimental attainment of optimum conditions" ; M. Hemavathi, Shashi Shekhar, Eldho Varghese, Seema Jaggi, Bikas Sinha & Nripes Kumar Mandal (2022) <DOI: 10.1080/03610926.2021.1944213>."Theoretical developments in response surface designs: an informative review and further thoughts".). Second order rotatable designs are the most prominent and popular class of designs used for process and product optimization trials but it is suitable for situations when all the number of levels for each factor is the same. In many practical situations, RSDs with asymmetric levels (J.S. Mehta and M.N. Das (1968). "Asymmetric rotatable designs and orthogonal transformations" ; M. Hemavathi, Eldho Varghese, Shashi Shekhar & Seema Jaggi (2020) <DOI: 10.1080/02664763.2020.1864817>. "Sequential asymmetric third order rotatable designs (SATORDs)" .) are more suitable as these designs explore more regions in the design space.This package contains functions named Asords() ,CCD_coded(), CCD_original(), SORD_coded() and SORD_original() for generating asymmetric/symmetric RSDs along with the randomized layout. It also contains another function named Pred.var() for generating the variance of predicted response as well as the moment matrix based on a second order model.
	"""
	
	cran = "AsymmetricSORDs" 

	version("1.0.0", md5="205e0600ad2c1eda8dad8c76b9eb2a53")

