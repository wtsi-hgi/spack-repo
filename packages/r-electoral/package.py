# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElectoral(RPackage):
	"""Allocating Seats Methods and Party System Scores

	Highest averages & largest remainders allocating seats methods and
    several party system scores.
    Implemented highest averages allocating seats methods are D'Hondt, Webster,
    Danish, Imperiali, Hill-Huntington, Dean, Modified Sainte-Lague,
    equal proportions and Adams.
    Implemented largest remainders allocating seats methods are Hare, Droop,
    Hangenbach-Bischoff, Imperial, modified Imperial and quotas & remainders.
    The main advantage of this package is that ties are always reported
    and not incorrectly allocated.
    Party system scores provided are competitiveness, concentration,
    effective number of parties, party nationalization score,
    party system nationalization score and volatility.
    References:
    Gallagher (1991) <doi:10.1016/0261-3794(91)90004-C>.
    Norris (2004, ISBN:0-521-82977-1).
    Consejo Nacional Electoral del Ecuador (2014)<http://cne.gob.ec/documents/Estadisticas/Atlas/ATLAS/CAPITULO%206%20web.pdf>.
    Laakso & Taagepera (1979) <https://journals.sagepub.com/doi/pdf/10.1177/001041407901200101>.
    Jones & Mainwaring (2003) <https://kellogg.nd.edu/sites/default/files/old_files/documents/304_0.pdf>.
    Pedersen (1979) <https://janda.org/c24/Readings/Pedersen/Pedersen.htm>.
    Golosov (2010) <https://ppq.sagepub.com/content/16/2/171.abstract>.
    Golosov (2014) <https://ppq.sagepub.com/content/early/2014/09/08/1354068814549342.abstract>.
	"""
	
	cran = "electoral" 

	version("0.1.3", md5="a9c43b76d2f2905bea703e85784530b9")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ineq", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
