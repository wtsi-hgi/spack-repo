# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyOpendde(PythonPackage):
    """Open-source, all-atom biomolecular foundation model."""

    homepage = "https://github.com/aurekaresearch/OpenDDE"
    pypi = "opendde/opendde-1.2.0-py3-none-any.whl"

    license("Apache-2.0")

    version("1.0.0", sha256="1382b52223ae895cefc5d3d09fd981441cbc9f9f1fd26ff0361b1dac69947d54", expand=False, url="https://files.pythonhosted.org/packages/28/76/7add8839c57f5851ac694aecfa6204bd2bc816a5b61bf8d6f2c8ab75a4b6/opendde-1.0.0-py3-none-any.whl")
    version("1.0.1", sha256="d05c076d6ef8ac6e2097f7f4ef0b1a2ac19b3a617db749f9a2eadcef4ad1c6e3", expand=False, url="https://files.pythonhosted.org/packages/f9/2d/450dfe9572dcd4330c7b69b455505e60a9aa7deb75c87e60ce9ad1c86d2d/opendde-1.0.1-py3-none-any.whl")
    version("1.0.2", sha256="77c09a1a542cf6378d7e7e368f3e8935d4f0ecba1cce82b24509dd40b00e19d8", expand=False, url="https://files.pythonhosted.org/packages/d7/1b/fe9911ce4b37f24af27e40826dfc3dc9638eb53d5bb1bc7b41b6447720d4/opendde-1.0.2-py3-none-any.whl")
    version("1.0.3", sha256="6cbf9628f45da16250d433d127cf2529199609b592b8bf36659cde67ada3796a", expand=False, url="https://files.pythonhosted.org/packages/7a/60/b4893ac6299f91107867af0152a761a4c8cceb7a26888beb938413b1935c/opendde-1.0.3-py3-none-any.whl")
    version("1.1.0", sha256="05ff4955a812004939bb21a4b9e14bb19f0f76798eca3a49cf7584f3dc7bf425", expand=False, url="https://files.pythonhosted.org/packages/1b/81/e0cc76455c8631970b95496acd198b24e6ecf44858b4e9e026223e74b3f8/opendde-1.1.0-py3-none-any.whl")
    version("1.1.1", sha256="94b193bd360e017c9cfab08d199ec9333cb2919a49fe1d9270c659c4b2efe544", expand=False, url="https://files.pythonhosted.org/packages/58/ca/4dc0bca000b84fb44dd45f2f17159ce3b2587d341ccb5f62b8755bf88a47/opendde-1.1.1-py3-none-any.whl")
    version("1.2.0", sha256="59686c8ef03a1f3ca37f7967bc2913e922f1d5b8ff9f6d3dc244973ea925cd99", expand=False, url="https://files.pythonhosted.org/packages/b9/29/361799f2f64ec60909908d27cf940ff5134452b234e9ec02616e19596a17/opendde-1.2.0-py3-none-any.whl")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.11:3.13", type=("build", "run"))
    depends_on("py-torch", type=("build", "run"))
    depends_on("py-click", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-ml-collections", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-rdkit", type=("build", "run"))
    depends_on("py-biopython", type=("build", "run"))
    depends_on("py-biotite", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-pydantic", type=("build", "run"))
    depends_on("py-optree", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-networkx", type=("build", "run"))
    depends_on("py-packaging", when="@1.0.1:", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            Executable(join_path(self.prefix.bin, "opendde"))("--help")
