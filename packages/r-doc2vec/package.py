# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDoc2vec(RPackage):
	"""Distributed Representations of Sentences, Documents and Topics

	Learn vector representations of sentences, paragraphs or documents by using the 'Paragraph Vector' algorithms,
    namely the distributed bag of words ('PV-DBOW') and the distributed memory ('PV-DM') model. 
    The techniques in the package are detailed in the paper "Distributed Representations of Sentences and Documents" by Mikolov et al. (2014), available at <arXiv:1405.4053>.
    The package also provides an implementation to cluster documents based on these embedding using a technique called top2vec. 
    Top2vec finds clusters in text documents by combining techniques to embed documents and words and density-based clustering.
    It does this by embedding documents in the semantic space as defined by the 'doc2vec' algorithm. Next it maps
    these document embeddings to a lower-dimensional space using the 'Uniform Manifold Approximation and Projection' (UMAP) clustering algorithm 
    and finds dense areas in that space using a 'Hierarchical Density-Based Clustering' technique (HDBSCAN). These dense
    areas are the topic clusters which can be represented by the corresponding topic vector which is an aggregate of the 
    document embeddings of the documents which are part of that topic cluster. In the same semantic space similar words can 
    be found which are representative of the topic.
    More details can be found in the paper 'Top2Vec: Distributed Representations of Topics' by D. Angelov available at <arXiv:2008.09470>. 
	"""
	
	homepage = "https://github.com/bnosac/doc2vec"
	cran = "doc2vec" 

	version("0.2.0", md5="6f7e1397e9d1bf7cc53d12d66c275d00")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
