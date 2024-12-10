from multiprocessing import Process

seeds = {} # value is found location id
seeds_paired = []
map_seed_to_soil = {}
map_soil_to_fertilizer = {}
map_fertilizer_to_water = {}
map_water_to_light = {}
map_light_to_temp = {}
map_temp_to_humidity = {}
map_humidity_to_location = {}
# map key = source start, value = list where [0] = dest start, [1] = range (including start)



def scanfile(file: str, pair_mode: bool = False):
    def split_into_mapping(line: str):
        v = line.split()
        ret = {}
        ret[int(v[1])] = [int(v[0]), int(v[2])]
        return ret
    
    global seeds
    global map_seed_to_soil
    global map_soil_to_fertilizer
    global map_fertilizer_to_water
    global map_water_to_light
    global map_light_to_temp
    global map_temp_to_humidity
    global map_humidity_to_location

    phase = 0 # 0 = seeds, 1 = seed-to-soil, 2 = soil-to-fertilizer
              # 3 = fertilizer-to-water, 4 = water-to-light
              # 5 = light-to-temperature, 6 = temp-to-humidity
              # 7 = humidity-to-location, 8 = done

    for line in open(file, "r"):
        if line.isspace():
            phase += 1
            continue

        match phase:
            case 0:
                temp = line.split(": ")[1].split()
                seeds = {int(seed): -1 for seed in temp}
                for i in range(0, len(temp), 2):
                    seeds_paired.append((int(temp[i]), int(temp[i]) + int(temp[i+1])))
            case 1:
                if line == "seed-to-soil map:\n": continue
                map_seed_to_soil |= split_into_mapping(line)
            case 2:
                if line == "soil-to-fertilizer map:\n": continue
                map_soil_to_fertilizer |= split_into_mapping(line)
            case 3:
                if line == "fertilizer-to-water map:\n": continue
                map_fertilizer_to_water |= split_into_mapping(line)
            case 4:
                if line == "water-to-light map:\n": continue
                map_water_to_light |= split_into_mapping(line)
            case 5:
                if line == "light-to-temperature map:\n": continue
                map_light_to_temp |= split_into_mapping(line)
            case 6:
                if line == "temperature-to-humidity map:\n": continue
                map_temp_to_humidity |= split_into_mapping(line)
            case 7:
                if line == "humidity-to-location map:\n": continue
                map_humidity_to_location |= split_into_mapping(line)
            case _:
                break

def main():

    total = 0
    scanfile("day5.txt", True)
    
    # Get the location for each seed
    mappings = [map_seed_to_soil, map_soil_to_fertilizer, map_fertilizer_to_water, map_water_to_light,
                map_light_to_temp, map_temp_to_humidity, map_humidity_to_location]

    # Pairless mode
    for seed in seeds:
        src = seed
        stage = 0

        for mapping in mappings:
            for map in mapping:
                src_range_end = map + mapping[map][1]
                if (map <= src < src_range_end):
                    src = mapping[map][0] + (src - map)
                    break

            if stage == 6: seeds[seed] = src
            stage += 1

    # Print the min location
    #print(min(seeds.values()))

    # Split seed ranges according to where the seed-to-soil maps split





    splitted = []
    for seed_range in seeds_paired:
        for map in map_seed_to_soil:
            if (seed_range[0] <= map < seed_range[1]):
                splitted.append((int(map), int(seed_range[1])))
    
    # Print the min location again
    print(min_loc)


if __name__ == "__main__":
    main()