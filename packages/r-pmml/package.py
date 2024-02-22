# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPmml(RPackage):
	"""Generate PMML for Various Models

	The Predictive Model Markup Language (PMML) is an XML-based language which provides a way for applications to define machine learning, statistical and data mining models and to share models between PMML compliant applications. More information about the PMML industry standard and the Data Mining Group can be found at <http://dmg.org/>. The generated PMML can be imported into any PMML consuming application, such as Zementis Predictive Analytics products. The package isofor (used for anomaly detection) can be installed with devtools::install_github("gravesee/isofor").
	"""
	
	homepage = "https://open-source.softwareag.com/r-pmml/"
	cran = "pmml" 

	version("2.5.2", md5="308980e1acaf29bc7663cf0be8b62e77")

	depends_on("r-xml", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
