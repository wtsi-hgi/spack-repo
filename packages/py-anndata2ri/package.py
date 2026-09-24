# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyAnndata2ri(PythonPackage):
    """Convert between AnnData and SingleCellExperiment"""
    
    homepage = "https://icb-anndata2ri.readthedocs-hosted.com/"
    pypi = "anndata2ri/anndata2ri-2.0.1-py3-none-any.whl" 

    import_modules = ["anndata2ri"]

    version("1.0", sha256="c392036ec92ad82bac1bb7edf4e871f093b4faa6708121463c2af954410343fc", expand=False, url="https://files.pythonhosted.org/packages/b7/09/34c48ce5b4e99d022dcde7e1643f4a9c1523fc91bb916b1c97891bdbdadd/anndata2ri-1.0-py3-none-any.whl")
    version("1.0.1", sha256="9f035cef8fba49aba504ba74fcfbb366b1e5ea2499bff5d99c9f13fa096eb130", expand=False, url="https://files.pythonhosted.org/packages/16/78/9c9d7f5d9ce4cca24c3532bd0bd4e9d57660f74599ad42ed8499d290d201/anndata2ri-1.0.1-py3-none-any.whl")
    version("1.0.2", sha256="38da642c09ab41071f2845db815397b173d1fb5df6fc2bd947f78a3bad25adcc", expand=False, url="https://files.pythonhosted.org/packages/0c/ed/c6122175ff99a09d8f4f18fd8ac63cd9608fd912f3c501f14a9a99700af7/anndata2ri-1.0.2-py3-none-any.whl")
    version("1.0.3", sha256="819a0fb7d4073c80ec5108d47675c2c43402b045e1c4deee1ad393d67f9ef9e7", expand=False, url="https://files.pythonhosted.org/packages/68/10/c19971f73d5a63f9e5393f73b74b73838bb5ebdb6b6fec54440d1b3a2bc9/anndata2ri-1.0.3-py3-none-any.whl")
    version("1.0.4", sha256="7b10501323ac29be1ee531100d12a3d4384e41551412c7e07e8e973a3ad24f8b", expand=False, url="https://files.pythonhosted.org/packages/7a/9f/77d96cc12345fcab6bcb361d6df3e2583e075bc0414052220124261c9a50/anndata2ri-1.0.4-py3-none-any.whl")
    version("1.0.5", sha256="0c17e7cf227a7d4ef06eb262d88202267b205044baa98948b566910460fb5ab4", expand=False, url="https://files.pythonhosted.org/packages/f8/65/899659011b0bfeddedef86dc92eda4936da34977de620f8f281c378addab/anndata2ri-1.0.5-py3-none-any.whl")
    version("1.0.6", sha256="371858384c3e87bd44438677a00e7c02df7e04a5c0fff9c6ce11076069bf2d07", expand=False, url="https://files.pythonhosted.org/packages/75/f6/548804d13145c134937de647ccc71fa51f6cfe442c16f3b9121578fda2c4/anndata2ri-1.0.6-py3-none-any.whl")
    version("1.1", sha256="e18e2b969dfb2749e39660e833dcf82acb378858d4432db28c595e6fd8595bfe", expand=False, url="https://files.pythonhosted.org/packages/25/38/15674b5221bdd29b69dc4283cfa38b6540c5c2b663c74353d786129aa5ab/anndata2ri-1.1-py3-none-any.whl")
    version("1.2", sha256="7c6ffbfbf54a5ea67fe39dfc7de6c5b52c06250d7c24144093935b0ada1689f6", expand=False, url="https://files.pythonhosted.org/packages/c4/76/6cf9b519084db794c1f0032f9b9e77f6c385d25db1d24d8e1ce20b18cd13/anndata2ri-1.2-py3-none-any.whl")
    version("1.3", sha256="ab21f61a431947e1bb745cd8eecc6f7383864cd5873151949fb4281331387ba4", expand=False, url="https://files.pythonhosted.org/packages/ac/98/db1bac23040802e6fd5219355f198fd2a87db011f9aeb6f3ee76f2038a46/anndata2ri-1.3-py3-none-any.whl")
    version("1.3.1", sha256="16409a82ccc8c9498afad84b59a966c21a647a6969de1c8cf707e0d90c8b9d19", expand=False, url="https://files.pythonhosted.org/packages/d5/d5/cf4e2362f106653fa67866f365796d50457e9a61e087887a06fa49dfea7a/anndata2ri-1.3.1-py3-none-any.whl")
    version("1.3.2", sha256="8baf5afee129a1a3f12f85d6978a9fb00c531b0473481ff76684ff99e3bdfdf6", expand=False, url="https://files.pythonhosted.org/packages/a4/a2/ff2f5c1d714fddd9dc933129db0554ffd71103e3c26f8152a94041945f20/anndata2ri-1.3.2-py3-none-any.whl")
    version("2.0", sha256="66c24b0a2a5df42ca101e8f02a145d75d35b06b0c2ff6898780159626f76498a", expand=False, url="https://files.pythonhosted.org/packages/29/65/2d75de27c4daa2f07e02ffae0dd58a6cb2df153f6a932946df62fcb1f08f/anndata2ri-2.0-py3-none-any.whl")
    version("2.0.1", sha256="af447e3aae2ac3ea495888ce08498fc988e9e2dc7f16e5880080e15dcd7598f6", expand=False, url="https://files.pythonhosted.org/packages/01/37/bba391a8a285ff7bdfc96314f4ca5e09c12f183384e30823a774e15c0144/anndata2ri-2.0.1-py3-none-any.whl")

    depends_on("py-setuptools", type=("build"))
    with default_args(type=("build", "run")):
        depends_on("python@3.11:")
        depends_on("py-anndata")
        depends_on("py-tzlocal")
        depends_on("py-get-version")
        depends_on("py-rpy2@3.0.1:")
        depends_on("py-scanpy")
        depends_on("py-sphinx@3.0:")
        depends_on("py-lxml")
        depends_on("py-pre-commit")
        depends_on("py-importlib-metadata")
        depends_on("py-importlib-resources")
        depends_on("py-sphinx-rtd-theme@0.5:")
        depends_on("py-pygments")
        depends_on("py-setuptools-scm")
        depends_on("py-ipython")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import anndata2ri")
