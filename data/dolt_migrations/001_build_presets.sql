-- Class presets ("custom builds", issue #17). Apply in the Dolt clone of longevity-genie/enhancement-bio
-- (dolt sql < this file), commit and push; the sync action then carries the tables into data/enhancement.db.
-- The three presets below are a DRAFT by the lead: best-graded playable genes per theme, each under the
-- 100-credit budget. Names and membership are the maintainer's to change (edit rows, no code change needed).
CREATE TABLE build_presets (
  preset_id TEXT NOT NULL,
  name TEXT NOT NULL,
  description TEXT,
  sort_order INT NOT NULL DEFAULT 0,
  PRIMARY KEY (preset_id)
);
CREATE TABLE build_preset_genes (
  preset_id VARCHAR(64) NOT NULL,
  gene_id VARCHAR(128) NOT NULL,
  position INT NOT NULL DEFAULT 0,
  PRIMARY KEY (preset_id, gene_id),
  FOREIGN KEY (preset_id) REFERENCES build_presets (preset_id),
  FOREIGN KEY (gene_id) REFERENCES genes (gene_id)
);
INSERT INTO build_presets VALUES
  ('guardian', 'Longevity Guardian', 'Best-evidenced longevity genes: Klotho, MGMT, CETP, SIRT6 and IGF1R variants.', 1),
  ('regenerator', 'Regenerator', 'Muscle, hearing, cartilage and telomere repair.', 2),
  ('survivor', 'Extreme Survivor', 'Radiation, drying-out, heat and altitude tolerance borrowed from other species.', 3);
INSERT INTO build_preset_genes VALUES
  ('guardian', 'klotho', 1), ('guardian', 'mgmt_p140k', 2), ('guardian', 'cetp_lof', 3),
  ('guardian', 'sirt6_cent_variant', 4), ('guardian', 'igf1r_het', 5),
  ('regenerator', 'fst344', 1), ('regenerator', 'atoh1_gfi1_pou4f3_haircell', 2),
  ('regenerator', 'fgf18_cartilage', 3), ('regenerator', 'tert', 4),
  ('survivor', 'sod2', 1), ('survivor', 'ppri_ppra', 2), ('survivor', 'pvlea', 3),
  ('survivor', 'sor_pyrococcus', 4), ('survivor', 'dsup', 5), ('survivor', 'epas1_tibetan', 6),
  ('survivor', 'mb_seal', 7);
