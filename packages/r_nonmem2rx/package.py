# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNonmem2rx(RPackage):
	"""'nonmem2rx' Converts 'NONMEM' Models to 'rxode2'

	'NONMEM' has been a tool for running nonlinear mixed
    effects models since the 80s and is still used today (Bauer 2019
    <doi:10.1002/psp4.12404>). This tool allows you to convert
    'NONMEM' models to 'rxode2' (Wang, Hallow and James (2016)
    <doi:10.1002/psp4.12052>) and with simple models 'nlmixr2' syntax
    (Fidler et al (2019) <doi:10.1002/psp4.12445>). The 'nlmixr2'
    syntax requires the residual specification to be included and it
    is not always translated. If available, the 'rxode2' model will
    read in the 'NONMEM' data and compare the simulation for the
    population model ('PRED') individual model ('IPRED') and residual
    model ('IWRES') to immediately show how well the translation is
    performing. This saves the model development time for people who are
    creating an 'rxode2' model manually.  Additionally, this package reads
    in all the information to allow simulation with uncertainty (that is the
    number of observations, the number of subjects, and the covariance
    matrix) with a 'rxode2' model.  This is complementary to the
    'babelmixr2' package that translates 'nlmixr2' models to 'NONMEM' and can
    convert the objects converted from 'nonmem2rx' to a full 'nlmixr2' fit.
	"""
	
	homepage = "https://nlmixr2.github.io/nonmem2rx/"
	cran = "nonmem2rx" 

	version("0.1.3", md5="38179e6a212344282d988883c07478cc")

	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-dparser", type=("build", "run"))
	depends_on("r-lotri", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rxode2@2.0.13:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-qs", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-rxode2parse", type=("build", "run"))
