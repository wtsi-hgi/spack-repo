# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpbk(RPackage):
	"""Inference and Prediction of Generic Physiologically-Based
Kinetic Models

	Fit and simulate any kind of
    physiologically-based kinetic ('PBK') models whatever the number of compartments.
    Moreover, it allows to account for any link between pairs of compartments, as
    well as any link of each of the compartments with the external medium. Such
    generic PBK models have today applications in pharmacology (PBPK models) to
    describe drug effects, in toxicology and ecotoxicology (PBTK models) to describe
    chemical substance effects. In case of exposure to a parent compound (drug or
    chemical) the 'rPBK' package allows to consider metabolites, whatever their number
    and their phase (I, II, ...). Last but not least, package 'rPBK' can also be used for
    dynamic flux balance analysis (dFBA) to deal with metabolic networks. See also
    Charles et al. (2022) <doi:10.1101/2022.04.29.490045>.
	"""
	
	homepage = "https://gitlab.in2p3.fr/mosaic-software/rPBK/"
	cran = "rPBK" 

	version("0.2.4", md5="e107e44c74725d85381bc43e3752e472")
	version("0.2.3", md5="b48ac041ec59da139ad5bd94e2251f03")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
