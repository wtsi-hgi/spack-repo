# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDsmmr(RPackage):
	"""Estimation and Simulation of Drifting Semi-Markov Models

	Performs parametric and non-parametric estimation and simulation of 
    drifting semi-Markov processes. The definition of parametric and non-parametric
    model specifications is also possible. Furthermore, three different types of
    drifting semi-Markov models are considered. These models differ in the number
    of transition matrices and sojourn time distributions used for the computation
    of a number of semi-Markov kernels, which in turn characterize the drifting 
    semi-Markov kernel. For the parametric model estimation and specification, 
    several discrete distributions are considered for the sojourn times: Uniform,
    Poisson, Geometric, Discrete Weibull and Negative Binomial. The non-parametric
    model specification makes no assumptions about the shape of the sojourn time
    distributions. Semi-Markov models are described in:
    Barbu, V.S., Limnios, N. (2008) <doi:10.1007/978-0-387-73173-5>.
    Drifting Markov models are described in:
    Vergne, N. (2008) <doi:10.2202/1544-6115.1326>.
    Reliability indicators of Drifting Markov models are described in:
    Barbu, V. S., Vergne, N. (2019) <doi:10.1007/s11009-018-9682-8>. 
    We acknowledge the DATALAB Project
    <https://lmrs-num.math.cnrs.fr/projet-datalab.html> (financed by the
    European Union with the European Regional Development fund (ERDF) and by
    the Normandy Region) and the HSMM-INCA Project (financed by the French
    Agence Nationale de la Recherche (ANR) under grant ANR-21-CE40-0005).
	"""
	
	cran = "dsmmR" 

	version("1.0.2", md5="1bc2f0ec552f1a806e5eeefd6ebdd443")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-discreteweibull", type=("build", "run"))
