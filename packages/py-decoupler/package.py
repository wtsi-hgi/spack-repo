# Copyright 2013-2023 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT file for
# details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDecoupler(PythonPackage):
    """Ensemble of methods to infer biological activities from omics data."""

    homepage = "https://decoupler.readthedocs.io/"
    pypi = "decoupler/decoupler-1.8.0-py3-none-any.whl"

    license("BSD-3-Clause")

    version(
        "2.1.4",
        sha256="356a6010676c8aa199e9e8286e405544d22f1dd8a14a840779c8734423720048",
        url="https://files.pythonhosted.org/packages/99/49/c2ebe5e019194095bb24f2285c5a6ce3bffae14c32cbdc4968d33aa2eb05/decoupler-2.1.4.tar.gz",
    )
    version(
        "1.8.0",
        sha256="726244bd809e70412ac82b51defc92b848b5a8f347084d1b4479d9b16ecd6228",
        expand=False,
        url="https://files.pythonhosted.org/packages/17/ea/30d51c7fd0edccf4c5e860a6e88f1f6f4d3bd141180a8caf7a57450c3c21/decoupler-1.8.0-py3-none-any.whl",
    )
    version(
        "1.7.0",
        sha256="44c5a8f001e5e1fa894f1ad54ce1476a035d54d44781faf3ebb40dae19a79bd9",
        expand=False,
        url="https://files.pythonhosted.org/packages/8e/78/7f4a2b593222017e0870266c1c4d189740a05208716e5dec93d686b54720/decoupler-1.7.0-py3-none-any.whl",
    )
    version(
        "1.6.0",
        sha256="aa65167a93f7bc79ce67c3ef320f19554ee1af857fd52acfa6d58fa2b0461912",
        expand=False,
        url="https://files.pythonhosted.org/packages/31/16/2804856d500b8ed683e9dadbba002f32eee284c5b2429256785f7de3478a/decoupler-1.6.0-py3-none-any.whl",
    )
    version(
        "1.5.0",
        sha256="c53d322ad4c57c91afb83b8a04da99db638820033e0b792b026890aee671073e",
        expand=False,
        url="https://files.pythonhosted.org/packages/94/43/b70d7c4fbce9e2a62f30d3b740a926e2ce99dcd85fcdad8756cce87d91ef/decoupler-1.5.0-py3-none-any.whl",
    )
    version(
        "1.4.0",
        sha256="5f34bf7c6d89479cac1a01a6483c86d4bb2f9c5ae870b8c42a1bac435e443c1e",
        expand=False,
        url="https://files.pythonhosted.org/packages/d9/83/8fb8f55794aa80a13f866f921ef98829643a9c88e7aeb88f8d5d57d0ac04/decoupler-1.4.0-py3-none-any.whl",
    )
    version(
        "1.3.4",
        sha256="1781d21ab2a99a17ec6c325e71f02bce876013050f0980456e6c2121d962062a",
        expand=False,
        url="https://files.pythonhosted.org/packages/fe/20/10c4cf8b71ab0e01969ce97279af63a9790c241b1fb8ad8efd20f778db78/decoupler-1.3.4-py3-none-any.whl",
    )
    version(
        "1.3.3",
        sha256="fbca3cd4945edf6a01f74904af4c5e507544e7fc1c4536a4fef9af8b053e6806",
        expand=False,
        url="https://files.pythonhosted.org/packages/16/f9/1c684fe1b687a1120b636adeb9ec5e3ce7744167d0b71e5ad3e9047dd976/decoupler-1.3.3-py3-none-any.whl",
    )
    version(
        "1.3.2",
        sha256="ef959e69d2ea8b6bfd1ae23326187300c8db651f2b44f963a13c82c62dc2b377",
        expand=False,
        url="https://files.pythonhosted.org/packages/c0/56/3117e9272fd9222c59ddc12355cc5d2fb8272d08df20aac429a8c6f58721/decoupler-1.3.2-py3-none-any.whl",
    )
    version(
        "1.3.1",
        sha256="980b48210d00f52815918eaa0ba303a7486fd437e7014c10c34a3217895ed2b3",
        expand=False,
        url="https://files.pythonhosted.org/packages/80/7a/36452015fefd68be93edd87d4bc31d50202cee58277ac97ff99e032d7641/decoupler-1.3.1-py3-none-any.whl",
    )
    version(
        "1.3.0",
        sha256="9b07eb2149e4986adb678da5249455c11ba65d62d64b45d59b16ee68e689c688",
        expand=False,
        url="https://files.pythonhosted.org/packages/9e/bd/ca2cdee5ce76d9779bce87342957f18e7160973bc0b39f6daf8f102e0044/decoupler-1.3.0-py3-none-any.whl",
    )
    version(
        "1.2.0",
        sha256="64aff47c7eecc10a4af5edc1cb942d6fb6e8939091abaa96465d6ec1f5c2b6ee",
        expand=False,
        url="https://files.pythonhosted.org/packages/d8/47/b0607de80a3d8c356787e982ecccd5960289223a5dcc27fb0a3a21f6f1aa/decoupler-1.2.0-py3-none-any.whl",
    )
    version(
        "1.1.0",
        sha256="5173fe7ffc6404f60066f93516bbab20b1c09141f7f5b84f073f8e43f72a16c4",
        expand=False,
        url="https://files.pythonhosted.org/packages/05/94/f2ae7e5ce796267d3a54094b945f83652884730a1fd63da97e99804877ee/decoupler-1.1.0-py3-none-any.whl",
    )
    version(
        "1.0.0",
        sha256="02a6730f26c1288248f5244c81410155c7c36e12e57c14664ff8a6750802aa43",
        expand=False,
        url="https://files.pythonhosted.org/packages/05/6d/f36d1071a12e13c26a02636061c4d680dd28495718a7b55d0d2e5733d8fe/decoupler-1.0.0-py3-none-any.whl",
    )

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("python@3.10:", when="@2:", type=("build", "run"))

    depends_on("py-hatchling", type="build", when="@2:")

    depends_on("py-adjusttext", when="@2:", type=("build", "run"))
    depends_on("py-anndata", when="@:1.6", type=("build", "run"))
    depends_on("py-anndata", when="@2:", type=("build", "run"))
    depends_on("py-docrep", when="@2:", type=("build", "run"))
    depends_on("py-marsilea", when="@2:", type=("build", "run"))
    depends_on("py-requests", when="@2:", type=("build", "run"))
    depends_on("py-scipy", when="@2:", type=("build", "run"))
    depends_on("py-session-info2", when="@2:", type=("build", "run"))

    depends_on("py-numba", type=("build", "run"))
    depends_on("py-numba@0.60:0.60", when="@1.7:1.8", type=("build", "run"))

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-numpy@1.0:1", when="@1.7:1.8", type=("build", "run"))

    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-pandas@2.2.2:", when="@1.7:1.8", type=("build", "run"))

    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-tqdm@4.66.4:", when="@1.7:1.8", type=("build", "run"))

    depends_on("py-typing-extensions", when="@1.3.1:1.8", type=("build", "run"))

    def patch(self):
        if self.spec.satisfies("@2:"):
            filter_file(
                r'\s*"Programming Language :: Python :: 3\.14",?\n',
                "",
                "pyproject.toml",
            )
