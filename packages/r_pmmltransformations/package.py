# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPmmltransformations(RPackage):
	"""Transforms Input Data from a PMML Perspective

	Allows for data to be transformed before using it to construct models. Builds structures to allow functions in the PMML package to
    output transformation details in addition to the model in the resulting PMML file. The Predictive Model Markup Language (PMML) is an XML-based language which provides a way for applications to define machine learning, statistical and data mining models and to share models between PMML compliant applications. More information about the PMML industry standard and the Data Mining Group can be found at <http://www.dmg.org>. The generated PMML can be imported into any PMML consuming application, such as Zementis Predictive Analytics products, which integrate with web services, relational database systems and deploy natively on Hadoop in conjunction with Hive, Spark or Storm, as well as allow predictive analytics to be executed for IBM z Systems mainframe applications and real-time, streaming analytics platforms.
	"""
	
	homepage = "https://www.softwareag.com/zementis"
	cran = "pmmlTransformations" 

	version("1.3.3", md5="f3057df6f847e13c063f8715550ac0e5")

