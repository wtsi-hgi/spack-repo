# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJmotif(RPackage):
	"""Time Series Analysis Toolkit Based on Symbolic Aggregate
Discretization, i.e. SAX

	Implements time series z-normalization, SAX, HOT-SAX, VSM, SAX-VSM, RePair, and RRA
    algorithms facilitating time series motif (i.e., recurrent pattern), discord (i.e., anomaly),
    and characteristic pattern discovery along with interpretable time series classification.
	"""
	
	homepage = "https://github.com/jMotif/jmotif-R"
	cran = "jmotif" 

	version("1.1.1", md5="ebaf99439838cd9ad3080a57e779337e")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
