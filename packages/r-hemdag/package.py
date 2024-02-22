# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHemdag(RPackage):
	"""Hierarchical Ensemble Methods for Directed Acyclic Graphs

	An implementation of several Hierarchical Ensemble Methods (HEMs) for Directed Acyclic Graphs (DAGs). 'HEMDAG' package: 1) reconciles flat predictions with the topology of the ontology; 2) can enhance the predictions of virtually any flat learning methods by taking into account the hierarchical relationships between ontology classes; 3) provides biologically meaningful predictions that always obey the true-path-rule, the biological and logical rule that governs the internal coherence of biomedical ontologies; 4) is specifically designed for exploiting the hierarchical relationships of DAG-structured taxonomies, such as the Human Phenotype Ontology (HPO) or the Gene Ontology (GO), but can be safely applied to tree-structured taxonomies as well (as FunCat), since trees are DAGs; 5) scales nicely both in terms of the complexity of the taxonomy and in the cardinality of the examples; 6) provides several utility functions to process and analyze graphs; 7) provides several performance metrics to evaluate HEMs algorithms. (Marco Notaro, Max Schubach, Peter N. Robinson and Giorgio Valentini (2017) <doi:10.1186/s12859-017-1854-y>).
	"""
	
	homepage = "https://hemdag.readthedocs.io"
	cran = "HEMDAG" 

	version("2.7.4", md5="0bbf6cb8dc06839fa5e636cc48d80bbc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-precrec", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
