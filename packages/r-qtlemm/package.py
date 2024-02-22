# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQtlemm(RPackage):
	"""QTL Mapping and Hotspots Detection

	
    For QTL mapping, it consists of several functions to perform various tasks, including 
    simulating or analyzing data, computing the significance thresholds and visualizing the 
    QTL mapping results. The single-QTL or multiple-QTL method that allows a host of 
    statistical models to be fitted and compared is applied to analyze the data for the 
    estimation of QTL parameters. The models include the linear regression, permutation test,
    normal mixture model and truncated normal mixture model. The Gaussian stochastic process
    is implemented to compute the significance thresholds for QTL detection onto a genetic 
    linkage map in the experimental populations. Two types of data, the complete genotyping 
    or selective genotyping data, from various experimental populations, including backcross,
    F2, recombinant inbred (RI) populations, and advanced intercrossed (AI) populations, are
    considered in the QTL mapping analysis. For QTL hotspot detection, the statistical methods
    can be developed based on either using the individual-level data or using the summarized
    data. We have proposed a statistical framework that can handle both the individual-level
    data and summarized QTL data for QTL hotspots detection. Our statistical framework can 
    overcome the underestimation of threshold arising from ignoring the correlation structure
    among traits, and also identify the different types of hotspots with very low 
    computational cost during the detection process. Here, we attempt to provide the R codes 
    of our QTL mapping and hotspot detection methods for general use in genes, genomics, and 
    genetics studies. The QTL mapping methods for the complete and selective genotyping 
    designs are based on the multiple interval mapping (MIM) model proposed by Kao, C.-H. ,
    Z.-B. Zeng and R. D. Teasdale (1999)  <doi: 10.1534/genetics.103.021642> and H.-I Lee,
    H.-A. Ho and C.-H. Kao (2014) <doi: 10.1534/genetics.114.168385>, respectively. The QTL 
    hotspot detection analysis is based on the method by Wu, P.-Y., M.-.H. Yang, and C.-H.
    Kao (2021) <doi: 10.1093/g3journal/jkab056>.
	"""
	
	homepage = "https://github.com/py-chung/QTLEMM"
	cran = "QTLEMM" 

	version("1.5.0", md5="ec895aba0a82d48f6cd6cfddfcb879a1")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
