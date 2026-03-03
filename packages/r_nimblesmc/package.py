# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNimblesmc(RPackage):
	"""Sequential Monte Carlo Methods for 'nimble'

	Includes five particle filtering algorithms for use with state space
    models in the 'nimble' system: 'Auxiliary', 'Bootstrap', 'Ensemble Kalman filter',
    'Iterated Filtering 2', and 'Liu-West', as described in Michaud et al. (2021),
    <doi:10.18637/jss.v100.i03>. A full User Manual is available at
    <https://r-nimble.org>.     
	"""
	
	homepage = "https://r-nimble.org"
	cran = "nimbleSMC" 

	version("0.11.0", md5="23246193123dc9cfed754435f149e965")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-nimble@1:", type=("build", "run"))
