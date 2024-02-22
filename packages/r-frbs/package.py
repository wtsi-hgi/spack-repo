# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrbs(RPackage):
	"""Fuzzy Rule-Based Systems for Classification and Regression Tasks

	An implementation of various learning algorithms based on fuzzy rule-based systems (FRBSs) for dealing with classification and regression tasks. Moreover, it allows to construct an FRBS model defined by human experts. 
    FRBSs are based on the concept of fuzzy sets, proposed by Zadeh in 1965, which aims at
    representing the reasoning of human experts in a set of IF-THEN rules, to
    handle real-life problems in, e.g., control, prediction and inference, data
    mining, bioinformatics data processing, and robotics. FRBSs are also known
    as fuzzy inference systems and fuzzy models. During the modeling of an
    FRBS, there are two important steps that need to be conducted: structure
    identification and parameter estimation. Nowadays, there exists a wide
    variety of algorithms to generate fuzzy IF-THEN rules automatically from
    numerical data, covering both steps. Approaches that have been used in the
    past are, e.g., heuristic procedures, neuro-fuzzy techniques, clustering
    methods, genetic algorithms, squares methods, etc. Furthermore, in this
    version we provide a universal framework named 'frbsPMML', which is adopted
    from the Predictive Model Markup Language (PMML), for representing FRBS
    models. PMML is an XML-based language to provide a standard for describing
    models produced by data mining and machine learning algorithms. Therefore,
    we are allowed to export and import an FRBS model to/from 'frbsPMML'.
    Finally, this package aims to implement the most widely used standard
    procedures, thus offering a standard package for FRBS modeling to the R
    community.
	"""
	
	homepage = "http://sci2s.ugr.es/dicits/software/FRBS"
	cran = "frbs" 

	version("3.2-0", md5="f58f112585984e5ae14d88b568f0a514")

