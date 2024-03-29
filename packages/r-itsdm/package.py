# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RItsdm(RPackage):
	"""Isolation Forest-Based Presence-Only Species Distribution
Modeling

	Collection of R functions to do purely presence-only species
    distribution modeling with isolation forest (iForest) and its
    variations such as Extended isolation forest and SCiForest. See the
    details of these methods in references: Liu, F.T., Ting, K.M. and
    Zhou, Z.H. (2008) <doi:10.1109/ICDM.2008.17>, Hariri, S., Kind, M.C.
    and Brunner, R.J. (2019) <doi:10.1109/TKDE.2019.2947676>, Liu, F.T.,
    Ting, K.M. and Zhou, Z.H. (2010) <doi:10.1007/978-3-642-15883-4_18>,
    Guha, S., Mishra, N., Roy, G. and Schrijvers, O. (2016)
    <https://proceedings.mlr.press/v48/guha16.html>, Cortes, D. (2021)
    <arXiv:2110.13402>. Additionally, Shapley values are used to explain
    model inputs and outputs. See details in references: Shapley, L.S.
    (1953) <doi:10.1515/9781400881970-018>, Lundberg, S.M. and Lee, S.I.
    (2017) <https://dl.acm.org/doi/abs/10.5555/3295222.3295230>, Molnar,
    C.  (2020) <ISBN:978-0-244-76852-2>, Štrumbelj, E. and Kononenko, I.
    (2014) <doi:10.1007/s10115-013-0679-x>. itsdm also provides functions
    to diagnose variable response, analyze variable importance, draw
    spatial dependence of variables and examine variable contribution. As
    utilities, the package includes a few functions to download
    bioclimatic variables including 'WorldClim' version 2.0 (see Fick,
    S.E. and Hijmans, R.J. (2017) <doi:10.1002/joc.5086>) and
    'CMCC-BioClimInd' (see Noce, S., Caporaso, L. and Santini, M. (2020)
    <doi:10.1038/s41597-020-00726-5>.
	"""
	
	homepage = "https://github.com/LLeiSong/itsdm"
	cran = "itsdm" 

	version("0.2.1", md5="15fb5225e04a71f22917d4e129e69447")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fastshap", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-isotree", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-outliertree", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rocit", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stars@0.6.0:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
