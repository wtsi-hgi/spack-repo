# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScreenot(RPackage):
	"""'ScreeNOT': MSE-Optimal Singular Value Thresholding in
Correlated Noise

	Optimal hard thresholding of singular values. The procedure adaptively estimates the best singular value threshold under unknown noise characteristics. The threshold chosen by 'ScreeNOT' is optimal (asymptotically, in the sense of minimum Frobenius error) under the the so-called "Spiked model" of a low-rank matrix observed in additive noise. In contrast to previous works, the noise is not assumed to be i.i.d. or white; it can have an essentially arbitrary and unknown correlation structure, across either rows, columns or both. 'ScreeNOT' is proposed to practitioners as a mathematically solid alternative to Cattell's ever-popular but vague Scree Plot heuristic from 1966. 
    If you use this package, please cite our paper: David L. Donoho, Matan Gavish and Elad Romanov (2023). "ScreeNOT: Exact MSE-optimal singular value thresholding in correlated noise." Annals of Statistics, 2023 (To appear). <arXiv:2009.12297>.
	"""
	
	cran = "ScreeNOT" 

	version("0.1.0", md5="d3ddea2451eb0d12f7076ebd5a37b886")

