# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenieclust(RPackage):
	"""Fast and Robust Hierarchical Clustering with Noise Points
Detection

	A retake on the Genie algorithm
    (Gagolewski, 2021 <DOI:10.1016/j.softx.2021.100722>) - a robust
    hierarchical clustering method
    (Gagolewski, Bartoszuk, Cena, 2016 <DOI:10.1016/j.ins.2016.05.003>).
    Now faster and more memory efficient; determining the whole hierarchy
    for datasets of 10M points in low dimensional Euclidean spaces or
    100K points in high-dimensional ones takes only 1-2 minutes.
    Allows clustering with respect to mutual reachability distances
    so that it can act as a noise point detector or a robustified version of
    'HDBSCAN*' (that is able to detect a predefined number of
    clusters and hence it does not dependent on the somewhat
    fragile 'eps' parameter).
    The package also features an implementation of inequality indices
    (the Gini, Bonferroni index), external cluster validity measures
    (e.g., the normalised clustering accuracy and partition similarity scores
    such as the adjusted Rand, Fowlkes-Mallows, adjusted mutual information,
    and the pair sets index),
    and internal cluster validity indices (e.g., the Calinski-Harabasz,
    Davies-Bouldin, Ball-Hall, Silhouette, and generalised Dunn indices).
    See also the 'Python' version of 'genieclust' available on 'PyPI', which
    supports sparse data, more metrics, and even larger datasets.
	"""
	
	homepage = "https://genieclust.gagolewski.com/"
	cran = "genieclust" 

	version("1.1.5-2", md5="125f1f9bee8664c716c5c50816969c29")

	depends_on("r-rcpp", type=("build", "run"))
