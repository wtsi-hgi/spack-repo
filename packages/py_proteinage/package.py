# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyProteinage(PythonPackage):
    """Proteinage: custom package installed via pre-built wheel."""

    homepage = "https://test.pypi.org/project/proteinage/"
    # We override the version with a wheel URL
    version(
        "0.1.13",
        sha256="0fd401f8b6b0a95aa99cab169339965e7f741929869f60f06e5ad718a42181af",
        url="https://test-files.pythonhosted.org/packages/76/73/7ee877bc566b7c1e0fa858c35c66b1ff15f5c5cf3addd5ad57793c63f7e4/proteinage-0.1.13-py3-none-any.whl",
        expand=False
    )

    depends_on("py-setuptools", type="build")
    depends_on("py-pip", type="build")
    depends_on("py-joblib", type=("build", "run"))
    depends_on("py-lightgbm@4.0.0", type=("build", "run"))
    depends_on("py-numpy@:1", type=("build", "run"))  # numpy < 2.0
    depends_on("py-pandas@2.0.0:", type=("build", "run"))
    depends_on("py-requests@2.28.2:", type=("build", "run"))
    depends_on("py-scikit-learn@1.3.0:", type=("build", "run"))
    depends_on("py-scipy@1.10.1:", type=("build", "run"))

    build_system_class = "PythonWheel"
