# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPmclust(RPackage):
	"""Parallel Model-Based Clustering using
Expectation-Gathering-Maximization Algorithm for Finite Mixture
Gaussian Model

	Aims to utilize model-based clustering (unsupervised)
        for high dimensional and ultra large data, especially in a distributed
        manner. The code employs 'pbdMPI' to perform a
        expectation-gathering-maximization algorithm
        for finite mixture Gaussian
        models. The unstructured dispersion matrices are assumed in the
        Gaussian models. The implementation is default in the single program
        multiple data programming model. The code can be executed
        through 'pbdMPI' and MPI' implementations such as 'OpenMPI'
        and 'MPICH'.
        See the High Performance Statistical Computing website
	<https://snoweye.github.io/hpsc/>
	for more information, documents and examples.
	"""
	
	homepage = "https://pbdr.org/"
	cran = "pmclust" 

	version("0.2-1", md5="00c4f79d9fc08bda8aff0f2a21663ccb")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-pbdmpi@0.4.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
