# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetmeta(RPackage):
	"""Network Meta-Analysis using Frequentist Methods

	A comprehensive set of functions providing frequentist methods for network meta-analysis (Balduzzi et al., 2023) <doi:10.18637/jss.v106.i02> and supporting Schwarzer et al. (2015) <doi:10.1007/978-3-319-21416-0>, Chapter 8 "Network Meta-Analysis":
 - frequentist network meta-analysis following Rücker (2012) <doi:10.1002/jrsm.1058>;
 - additive network meta-analysis for combinations of treatments (Rücker et al., 2020) <doi:10.1002/bimj.201800167>;
 - network meta-analysis of binary data using the Mantel-Haenszel or non-central hypergeometric distribution method (Efthimiou et al., 2019) <doi:10.1002/sim.8158>;
 - rankograms and ranking of treatments by the Surface under the cumulative ranking curve (SUCRA) (Salanti et al., 2013) <doi:10.1016/j.jclinepi.2010.03.016>;
 - ranking of treatments using P-scores (frequentist analogue of SUCRAs without resampling) according to Rücker & Schwarzer (2015) <doi:10.1186/s12874-015-0060-8>;
 - split direct and indirect evidence to check consistency (Dias et al., 2010) <doi:10.1002/sim.3767>, (Efthimiou et al., 2019) <doi:10.1002/sim.8158>;
 - league table with network meta-analysis results;
 - 'comparison-adjusted' funnel plot (Chaimani & Salanti, 2012) <doi:10.1002/jrsm.57>;
 - net heat plot and design-based decomposition of Cochran's Q according to Krahn et al. (2013) <doi:10.1186/1471-2288-13-35>;
 - measures characterizing the flow of evidence between two treatments by König et al. (2013) <doi:10.1002/sim.6001>;
 - automated drawing of network graphs described in Rücker & Schwarzer (2016) <doi:10.1002/jrsm.1143>;
 - partial order of treatment rankings ('poset') and Hasse diagram for 'poset' (Carlsen & Bruggemann, 2014) <doi:10.1002/cem.2569>; (Rücker & Schwarzer, 2017) <doi:10.1002/jrsm.1270>;
 - contribution matrix as described in Papakonstantinou et al. (2018) <doi:10.12688/f1000research.14770.3> and Davies et al. (2022) <doi:10.1002/sim.9346>.
	"""
	
	homepage = "https://github.com/guido-s/netmeta"
	cran = "netmeta" 

	version("2.9-0", md5="37b2df89df7e99e90df1038ee2abfb47")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-meta@6.2.0:", type=("build", "run"))
	depends_on("r-magic", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
