# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTgs(RPackage):
	"""Rapid Reconstruction of Time-Varying Gene Regulatory Networks

	Rapid advancements in high-throughput gene sequencing
    technologies have resulted in genome-scale time-series datasets. 
    Uncovering the underlying temporal sequence of gene regulatory events 
    in the form of time-varying gene regulatory networks demands 
    accurate and computationally efficient algorithms. Such an
    algorithm is 'TGS'. It is proposed in Saptarshi Pyne, Alok Ranjan 
    Kumar, and Ashish Anand. Rapid reconstruction of time-varying 
    gene regulatory networks. IEEE/ACM Transactions on Computational 
    Biology and Bioinformatics, 17(1):278{291, Jan-Feb 2020. The TGS 
    algorithm is shown to consume only 29 minutes for a microarray 
    dataset with 4028 genes. This package provides an implementation 
    of the TGS algorithm and its variants.
	"""
	
	homepage = "https://www.biorxiv.org/content/early/2018/06/14/272484"
	cran = "TGS" 

	version("1.0.1", md5="fbe95f1b5c1c7a332cb5350418508d5e")

	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-bnstruct", type=("build", "run"))
	depends_on("r-ggm", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-minet@3.38:", type=("build", "run"))
