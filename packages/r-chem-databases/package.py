# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChemDatabases(RPackage):
	"""Collection of 3 Chemical Databases from Public Sources

	Contains the Multi-Species Acute Toxicity Database (CAS & SMILES
    columns only) [United States (US) Department of Health and Human Services
    (DHHS) National Institutes of Health (NIH) National Cancer Institute (NCI),
    "Multi-Species Acute Toxicity Database",
    <https://cactus.nci.nih.gov/download/acute-toxicity-db/>] combined with the
    Toxic Substances Control Act (TSCA) Inventory [United States Environmental
    Protection Agency (US EPA), "Toxic Substances Control Act (TSCA) Chemical
    Substance Inventory",
    <https://www.epa.gov/tsca-inventory/how-access-tsca-inventory} and
    <https://cdxapps.epa.gov/oms-substance-registry-services/substance-list-details/169>]
    and the Agency for Toxic Substances and Disease Registry (ATSDR) Database
    [United States (US) Department of Health and Human Services (DHHS) Centers
    for Disease Control and Prevention (CDC)/Agency for Toxic Substances and
    Disease Registry (ATSDR), "Agency for Toxic Substances and Disease Registry
    (ATSDR) Database",
    <https://cdxapps.epa.gov/oms-substance-registry-services/substance-list-details/105>]
    in 2 data sets. One data set has a focus on the latter 2 databases and one
    data set focuses on the former database. Also contains the collection of
    chemical data from Wikipedia compiled in the US EPA CompTox Chemicals
    Dashboard [United States Environmental Protection Agency (US EPA) /
    Wikimedia Foundation, Inc. "CompTox Chemicals Dashboard v2.2.1",
    <https://comptox.epa.gov/dashboard/chemical-lists/WIKIPEDIA>].
	"""
	
	homepage = "https://gitlab.com/iembry/chem.databases"
	cran = "chem.databases" 

	version("1.0.0", md5="2b05ec4dc3597d97fbb1a3afbf9d6b26")

	depends_on("r@3.5:", type=("build", "run"))
