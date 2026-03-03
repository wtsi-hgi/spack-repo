# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTserieschaos(RPackage):
	"""Analysis of Nonlinear Time Series

	Routines for the analysis of nonlinear time series. This
        work is largely inspired by the TISEAN project, by Rainer
        Hegger, Holger Kantz and Thomas Schreiber:
        <http://www.mpipks-dresden.mpg.de/~tisean/>.
	"""
	
	cran = "tseriesChaos" 

	version("0.1-13.1", md5="a6a6c2a9ad7174c4e7bd046afee70da3")

	depends_on("r@2.2:", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
