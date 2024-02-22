# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTords(RPackage):
	"""Third Order Rotatable Designs (TORDs)

	Third order response surface designs (M. Hemavathi, Shashi Shekhar, Eldho Varghese, Seema Jaggi, Bikas Sinha & Nripes Kumar Mandal (2022) <DOI:10.1080/03610926.2021.1944213>."Theoretical developments in response surface designs: an informative review and further thoughts") are classified into two types viz., designs which are suitable for sequential experimentation and designs for non-sequential experimentation (M. Hemavathi, Eldho Varghese, Shashi Shekhar & Seema Jaggi (2022)<DOI:10.1080/02664763.2020.1864817>." Sequential asymmetric third order rotatable designs (SATORDs)"). The sequential experimentation approach involves conducting the trials step by step whereas, in the non-sequential experimentation approach, the entire runs are executed in one go.This package contains functions named STORDs() and NSTORDs() for generating sequential/non-sequential TORDs given in Das, M. N., and V. L. Narasimham (1962). <DOI:10.1214/aoms/1177704374>. "Construction of rotatable designs through balanced incomplete block designs" along with the randomized layout. It also contains another function named Pred3.var() for generating the variance of predicted response as well as the moment matrix based on a third order response surface model.
	"""
	
	cran = "TORDs" 

	version("1.0.0", md5="b5e09c69856a68c3a63493f410ad79d7")

	depends_on("r@2.10:", type=("build", "run"))
