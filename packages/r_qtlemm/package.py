# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQtlemm(RPackage):
	"""QTL Mapping and Hotspots Detection

	
    For QTL mapping, this package comprises several functions designed to execute diverse 
    tasks, such as simulating or analyzing data, calculating significance thresholds, and 
    visualizing QTL mapping results. The single-QTL or multiple-QTL method, which enables 
    the fitting and comparison of various statistical models, is employed to analyze the 
    data for estimating QTL parameters. The models encompass linear regression, permutation 
    tests, normal mixture models, and truncated normal mixture models. The Gaussian stochastic 
    process is utilized to compute significance thresholds for QTL detection on a genetic 
    linkage map within experimental populations. Two types of data, complete genotyping, and 
    selective genotyping data from various experimental populations, including backcross, F2, 
    recombinant inbred (RI) populations, and advanced intercrossed (AI) populations, are 
    considered in the QTL mapping analysis. For QTL hotspot detection, statistical methods can 
    be developed based on either utilizing individual-level data or summarized data. We have 
    proposed a statistical framework capable of handling both individual-level data and 
    summarized QTL data for QTL hotspot detection. Our statistical framework can overcome the 
    underestimation of thresholds resulting from ignoring the correlation structure among 
    traits. Additionally, it can identify different types of hotspots with minimal computational 
    cost during the detection process. Here, we endeavor to furnish the R codes for our QTL 
    mapping and hotspot detection methods, intended for general use in genes, genomics, and 
    genetics studies. The QTL mapping methods for the complete and selective genotyping designs 
    are based on the multiple interval mapping (MIM) model proposed by Kao, C.-H. , Z.-B. Zeng 
    and R. D. Teasdale (1999) <doi: 10.1534/genetics.103.021642> and H.-I Lee, H.-A. Ho and 
    C.-H. Kao (2014) <doi: 10.1534/genetics.114.168385>, respectively. The QTL hotspot detection 
    analysis is based on the method by Wu, P.-Y., M.-.H. Yang, and C.-H. Kao (2021) 
    <doi: 10.1093/g3journal/jkab056>.
	"""
	
	homepage = "https://github.com/py-chung/QTLEMM"
	cran = "QTLEMM" 

	version("1.5.2", md5="bccc56759dc619aa019f0207223b11a6")
	version("1.5.0", md5="ec895aba0a82d48f6cd6cfddfcb879a1")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
