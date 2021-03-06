#!/usr/bin/env python
#JSON {"lot": "UHF/3-21G",
#JSON  "scf": "PlainSCFSolver",
#JSON  "er": "dense",
#JSON  "difficulty": 1,
#JSON  "description": "Basic UHF example with dense matrices"}

from horton import *  # pylint: disable=wildcard-import,unused-wildcard-import


# Load the coordinates from file.
# Use the XYZ file from HORTON's test data directory.
fn_xyz = context.get_fn('test/methyl.xyz')
mol = IOData.from_file(fn_xyz)

# Create a Gaussian basis set
obasis = get_gobasis(mol.coordinates, mol.numbers, '3-21G')

# Compute Gaussian integrals
olp = obasis.compute_overlap()
kin = obasis.compute_kinetic()
na = obasis.compute_nuclear_attraction(mol.coordinates, mol.pseudo_numbers)
er_vecs = obasis.compute_electron_repulsion()

# Create alpha orbitals
orb_alpha = Orbitals(obasis.nbasis)
orb_beta = Orbitals(obasis.nbasis)

# Initial guess
guess_core_hamiltonian(olp, kin + na, orb_alpha, orb_beta)

# Construct the restricted HF effective Hamiltonian
external = {'nn': compute_nucnuc(mol.coordinates, mol.pseudo_numbers)}
terms = [
    UTwoIndexTerm(kin, 'kin'),
    UDirectTerm(er_vecs, 'hartree'),
    UExchangeTerm(er_vecs, 'x_hf'),
    UTwoIndexTerm(na, 'ne'),
]
ham = UEffHam(terms, external)

# Decide how to occupy the orbitals (5 alpha electrons, 4 beta electrons)
occ_model = AufbauOccModel(5, 4)

# Converge WFN with plain SCF
scf_solver = PlainSCFSolver(1e-6)
scf_solver(ham, olp, occ_model, orb_alpha, orb_beta)

# Assign results to the molecule object and write it to a file, e.g. for
# later analysis
mol.title = 'UHF computation on methyl'
mol.energy = ham.cache['energy']
mol.obasis = obasis
mol.orb_alpha = orb_alpha
mol.orb_beta = orb_beta

# useful for visualization:
mol.to_file('methyl.molden')
# useful for post-processing (results stored in double precision)
mol.to_file('methyl.h5')


# CODE BELOW IS FOR horton-regression-test.py ONLY. IT IS NOT PART OF THE EXAMPLE.
rt_results = {
    'energy': ham.cache['energy'],
    'orb_alpha': orb_alpha.energies,
    'orb_beta': orb_beta.energies,
    'nn': ham.cache["energy_nn"],
    'kin': ham.cache["energy_kin"],
    'ne': ham.cache["energy_ne"],
    'ex': ham.cache["energy_x_hf"],
    'hartree': ham.cache["energy_hartree"],
}
# BEGIN AUTOGENERATED CODE. DO NOT CHANGE MANUALLY.
import numpy as np  # pylint: disable=wrong-import-position
rt_previous = {
    'energy': -39.331221904962412,
    'ex': -6.113904009056378,
    'orb_alpha': np.array([
        -11.194977911345202, -0.92420112228138784, -0.55513937861886831,
        -0.55513936656337781, -0.38934656780805416, 0.2535844073284213,
        0.33566480311154712, 0.3356648206159526, 0.9332291232904848, 0.98518834644331721,
        0.98518849306172951, 1.102449080416404, 1.3032622584429283, 1.3032623363395135,
        1.6761192066890211
    ]),
    'orb_beta': np.array([
        -11.169031571491915, -0.81817737275326963, -0.53903034297663222,
        -0.53903033685265866, 0.16303091192059521, 0.28378927314962432,
        0.34897199801702861, 0.34897201610275758, 1.0010276475405682, 1.0010277998402939,
        1.0836169709197594, 1.1060903534350119, 1.3066657923992548, 1.3066658801221429,
        1.7272407098243059
    ]),
    'hartree': 27.840836401008165,
    'kin': 38.93357262027515,
    'ne': -109.07151185985299,
    'nn': 9.0797849426636361,
}
