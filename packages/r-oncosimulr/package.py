# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROncosimulr(RPackage):
    """Forward Genetic Simulation of Cancer Progression with Epistasis

    Functions for forward population genetic simulation in asexual populations, with special focus on cancer progression. Fitness can be an arbitrary function of genetic interactions between multiple genes or modules of genes, including epistasis, order restrictions in mutation accumulation, and order effects. Fitness (including just birth, just death, or both birth and death) can also be a function of the relative and absolute frequencies of other genotypes (i.e., frequency-dependent fitness). Mutation rates can differ between genes, and we can include mutator/antimutator genes (to model mutator phenotypes). Simulating multi-species scenarios and therapeutic interventions, including adaptive therapy, is also possible. Simulations use continuous-time models and can include driver and passenger genes and modules. Also included are functions for: simulating random DAGs of the type found in Oncogenetic Trees, Conjunctive Bayesian Networks, and other cancer progression models; plotting and sampling from single or multiple realizations of the simulations, including single-cell sampling; plotting the parent-child relationships of the clones; generating random fitness landscapes (Rough Mount Fuji, House of Cards, additive, NK, Ising, and Eggbox models) and plotting them.
    """

    homepage = "https://github.com/rdiaz02/OncoSimul"
    bioc = "OncoSimulR"

    version("4.10.0", commit="165d213a528650622e941e243a4d5e5baa12999a")
    version("4.4.0", commit="c736f65ce9373e8d9cba8eb4122d1075ac752eed")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-graph", type=("build", "run"))
    depends_on("r-rgraphviz", type=("build", "run"))
    depends_on("r-gtools", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-car", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-smatr", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
