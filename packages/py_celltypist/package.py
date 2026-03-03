# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCelltypist(PythonPackage):
    """CellTypist is an automated cell type annotation tool for scRNA-seq datasets on the basis of logistic regression classifiers optimised by the stochastic gradient descent algorithm. CellTypist allows for cell prediction using either built-in (with a current focus on immune sub-populations) or custom models, in order to assist in the accurate classification of different cell types and subtypes."""

    homepage = "https://www.celltypist.org/"

    url = "https://github.com/Teichlab/celltypist/archive/refs/tags/1.6.2.tar.gz"

    version("1.6.2", sha256="25a6409b80c739e772e5726aa50248aa9f5f7aaa266979ab011db6a76ab8894b")
    version("1.6.1", sha256="233da5ff9bc9ba794c8c67329329e40c6fd0bc528045580703abd03beb0eeadf")
    version("1.6.0", sha256="90d31597ce8be4f5b5c216245548e7c78abcfad6a720fd6ce43c34a12e687d48")
    version("1.5.3", sha256="90fff4fa5ca0e6b7e3a3a9391d1d97c8452580551b011419277624306f525dc8")
    version("1.5.2", sha256="d6ea545f89878186a203cd12efa5a7d279cc2a32ebf6c754ddade770b585cc11")
    version("1.5.1", sha256="a97c6050b7614432b7cbd77b967d78155f5a0e637d47e7f5fe01e7e8e0d179df")
    version("1.5.0", sha256="dbbb9aab5a4ef2735cf9c77db1d192478f0340bfd0db3da214e6ea100ee1be49")
    version("1.4.0", sha256="20e0c7d783c3cd97c0be2b097ebfde3516a0b9ec6f6dc10ab944a961c73e55d1")
    version("1.3.0", sha256="e9c9a5d6ed922d1a421cafe69ee4862f574b372806cc25ea67189f6f3ca0e524")
    version("1.2.0", sha256="2f22b8b8687ef53e93ad2d2e74a1e2ce16b046afe5de1597d834c1cc33985799")

    depends_on("py-setuptools", type="build")

    depends_on("py-numpy@1.19.0:", type=("build", "run"))
    depends_on("py-pandas@1.0.5:", type=("build", "run"))
    depends_on("py-scikit-learn@0.24.1:", type=("build", "run"))
    depends_on("py-openpyxl@3.0.4:", type=("build", "run"))
    depends_on("py-click@7.1.2:", type=("build", "run"))
    depends_on("py-requests@2.23.0:", type=("build", "run"))
    depends_on("py-scanpy@1.7.0:", type=("build", "run"))
    depends_on("py-leidenalg@0.9.0:", type=("build", "run"))
